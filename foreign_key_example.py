from models import *

# Use FK!!
applicants = Applicant.select()
for app in applicants:
    for interview in app.applicants_interviews:
        # azért kell if, mert nincsen minden applicant-nak interview_slotja
        if interview.slot_id is not None:
            print(interview.slot_id.start_time)

# Another example
schools = School.select()
for school in schools:
    for app in school.applicants:
        print(app.first_name)
