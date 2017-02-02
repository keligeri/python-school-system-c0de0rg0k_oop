from peewee import *
from set_connection import SetConnection

# Configure the database connection
connected = SetConnection()
db = PostgresqlDatabase(connected.dbname, user=connected.username)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class School(BaseModel):
    city = CharField()


class City(BaseModel):
    city_name = CharField()
    nearest_school = ForeignKeyField(School, related_name='cities')


class Applicant(BaseModel):
    first_name = CharField()
    last_name = CharField()
    applicant_city = CharField()
    applicant_code = CharField(null=True)
    applied_school = ForeignKeyField(School, null=True, related_name='applicants')
    status = CharField(null=True)


class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related_name='mentor_school_city')


class InterviewSlot(BaseModel):
    start_time = DateTimeField()
    end_time = DateTimeField()
    reserved = BooleanField()
    mentor = ForeignKeyField(Mentor, related_name='interviewslot_mentor_id')


class Interview(BaseModel):
    slot_id = ForeignKeyField(InterviewSlot, null=True, related_name='interview_interviewslot_id')
    applicant_code = ForeignKeyField(Applicant, related_name='interviews')
