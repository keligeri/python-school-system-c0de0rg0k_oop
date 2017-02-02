from models import *
import random

query = InterviewSlot.select()

for slot in query:
    print (slot.start_time, "  ", slot.reserved, slot.mentor.last_name)

interviews = Interview.select()
for interview in interviews:
    print (interview.applicant_code.applied_school.city)
