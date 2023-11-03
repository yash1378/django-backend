from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Mentor,Owner,MentorCred,RenrollData

# Create your views here.
def data(request):
    info = Student.objects.all()
    info1 = [{"name": i.name, "phone": i.phone, "email": i.email, "date": i.date, "_class": i._class, "subject": i.subject, "mentor": i.mentor} for i in info]
    return JsonResponse(info1, safe=False)


@csrf_exempt
def mentorData(request):
    try:
        if request.method == 'GET':
            conditions = request.GET  # Query parameters for conditions
            # You can access query parameters using request.GET.get('parameter_name')

            # Filter data in the Mentor model based on query parameters
            data = Mentor.objects.filter(**conditions).values()  # Convert to a dictionary
            return JsonResponse(list(data), safe=False)
        
        elif request.method == 'POST':
            requestdata = json.loads(request.body)
            if requestdata['name'] == "" or requestdata['phone'] == "" or requestdata['college'] == "" or requestdata['date'] == "" or requestdata['email'] == "" or requestdata['password'] == "":
                return JsonResponse({'message': 'Please fill all the fields', 'data': None}, status=400)
            
            # Check if a record with the same phone number already exists
            existing_record = Mentor.objects.filter(phone=requestdata['phone']).first()
            if existing_record:
                return JsonResponse({'message': 'Record with the same phone number already exists', 'data': None}, status=400)
            
            
            instance = Mentor(
                name=requestdata['name'],
                phone=requestdata['phone'],
                college=requestdata['college'],
                date=requestdata['date'],
                handle=0,
                total=0,
                on=0,
            )
            instance.save()
            
            cred = MentorCred(
                email=requestdata['email'],
                password=requestdata['password'],
                mentorname=requestdata['name'],
            )
            cred.save()
            
            return JsonResponse({'message': 'Data received on the server', 'data': requestdata}, status=200)
    except Exception as error:
        print("An error occurred:", error)
        return JsonResponse({"error": "An error occurred while fetching data."}, status=500)
    
    
    
@csrf_exempt
def ownerData(request):
    try:
        conditions = request.GET  # Query parameters for conditions
        # You can access query parameters using request.GET.get('parameter_name')

        # Filter data in the Own model based on query parameters
        data = Owner.objects.filter(**conditions).values()  # Convert to a dictionary

        return JsonResponse(list(data), safe=False)
    except Exception as error:
        print("An error occurred:", error)
        return JsonResponse({"error": "An error occurred while fetching data."}, status=500)

@csrf_exempt
def main(request):
    if request.method == 'POST':
        try:
            requestdata = json.loads(request.body)
            phone_number = requestdata['phone']

            # Check if a record with the same phone number already exists
            existing_record = Student.objects.filter(phone=phone_number).first()

            if existing_record:
                return JsonResponse({'message': 'Record with the same phone number already exists', 'data': None}, status=400)

            instance = Student(
                name=requestdata['name'],
                phone=phone_number,
                email=requestdata['email'],
                date=requestdata['date'],
                _class=requestdata['class'],
                subject=requestdata['sub'],
                mentor=""
            )
            instance.save()
            
            newinstance = RenrollData(
                name=requestdata['name'],
                phone=requestdata['phone'],
                email=requestdata['email'],
                date=requestdata['date'],
                _class=requestdata['class'],
                subject=requestdata['sub'],
                mentor="",
                renrollment=0,
            )
            newinstance.save()
            return JsonResponse({'message': 'Data received on the server', 'data': requestdata}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
    if request.method == 'GET':
        return HttpResponse("Hello, world. You're at the polls index.")
    

@csrf_exempt
def student(request, phone):
        # Get data from the request
    if request.method == 'POST':
        requestdata = json.loads(request.body)

        try:

            user = Student.objects.get(phone=phone)
            ment = Mentor.objects.get(name=user.mentor)
            new_ment = Mentor.objects.get(name=requestdata['newmentor'])


            if requestdata['studentName']:
                user.name = requestdata['studentName']
            if requestdata['studentEmail']:
                user.email = requestdata['studentEmail']
            if requestdata['phoneNumber']:
                user.phone = requestdata['phoneNumber']
            if requestdata['selectedClass']:
                user._class = requestdata['selectedClass']
            if requestdata['selectedDate']:
                user.date = requestdata['selectedDate']
            if requestdata['newmentor']:
                ment.on = ment.on - 1
                new_ment.on = new_ment.on + 1
                user.mentor = requestdata['newmentor']

            user.save()
            ment.save()
            new_ment.save()

            # Respond with a success message
            return JsonResponse({'message': 'UserData updated successfully'})

        except Student.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            print(f'An error occurred while updating data: {str(e)}')
            return JsonResponse({'error': 'Internal server error'}, status=500)

@csrf_exempt
def finalMentor(self, request):
    if request.method == 'POST':
        try:
            data =json.loads(request.body)
            mentor_name = data.get('mentorName')
            student_ids = data.getlist('studentPhoneNumbers[]')  # Use getlist to get multiple values

            students = Student.objects.filter(phone=student_ids)

            # Extract an array of phone numbers from the 'students' queryset
            phone_numbers = [student.phone for student in students]

            # Update students in the Student table
            students.update(mentor=mentor_name)

            # Update students in the Reuser table based on phone numbers
            RenrollData.objects.filter(phone__in=phone_numbers).update(mentor=mentor_name)

            # Get the count of selected students
            selected_student_count = len(student_ids)

            # Update the 'on' and 'total' fields for the mentor in the Mentor table
            mentor_to_update = Mentor.objects.get(name=mentor_name)
            mentor_to_update.on += selected_student_count
            mentor_to_update.total += selected_student_count
            mentor_to_update.save()

            # Respond with a success message
            return JsonResponse({'message': 'Mentor and students updated successfully'})

        except Student.DoesNotExist:
            return JsonResponse({'error': 'One or more students not found'}, status=404)
        except Mentor.DoesNotExist:
            return JsonResponse({'error': 'Mentor not found'}, status=404)
        except Exception as e:
            print(f'An error occurred while updating data: {str(e)}')
            return JsonResponse({'error': 'Internal server error'}, status=500)