from models import *

# Use FK!!
applicants = Applicant.select()
for app in applicants:
    for interview in app.applicants_interviews:
        if interview.slot_id is not None:   # need it, because hasn't got interview_slot for every applicants
            print(interview.slot_id.start_time)

# Another example
schools = School.select()
for school in schools:
    for app in school.applicants:
        print(app.first_name)
