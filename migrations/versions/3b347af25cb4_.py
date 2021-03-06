"""empty message

Revision ID: 3b347af25cb4
Revises: 04321feb1c9b
Create Date: 2018-04-18 18:35:10.644189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b347af25cb4'
down_revision = '04321feb1c9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Dorm_Room',
    sa.Column('dorm_name', sa.String(length=60), nullable=False),
    sa.Column('dorm_room_no', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('dorm_name', 'dorm_room_no')
    )
    op.create_table('Faculty',
    sa.Column('faculty_id', sa.Integer(), nullable=False),
    sa.Column('faculty_name', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('faculty_id')
    )
    op.create_table('Semester',
    sa.Column('semester_no', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('enroll_start_date', sa.Date(), nullable=True),
    sa.Column('enroll_end_date', sa.Date(), nullable=True),
    sa.Column('withdraw_start_date', sa.Date(), nullable=True),
    sa.Column('withdraw_end_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('semester_no', 'year')
    )
    op.create_table('Building',
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('faculty_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['faculty_id'], ['Faculty.faculty_id'], ),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('Major',
    sa.Column('major_id', sa.Integer(), nullable=False),
    sa.Column('faculty_id', sa.Integer(), nullable=False),
    sa.Column('major_name', sa.String(length=60), nullable=True),
    sa.ForeignKeyConstraint(['faculty_id'], ['Faculty.faculty_id'], ),
    sa.PrimaryKeyConstraint('major_id', 'faculty_id')
    )
    op.create_table('Student',
    sa.Column('sid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('enroll_year', sa.Integer(), nullable=True),
    sa.Column('graduated', sa.Boolean(), nullable=True),
    sa.Column('degree', sa.String(length=60), nullable=True),
    sa.Column('gpax', sa.Float(), nullable=True),
    sa.Column('dorm_score', sa.Integer(), nullable=True),
    sa.Column('dorm_name', sa.String(length=60), nullable=True),
    sa.Column('dorm_room_no', sa.Integer(), nullable=True),
    sa.Column('faculty_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dorm_name', 'dorm_room_no'], ['Dorm_Room.dorm_name', 'Dorm_Room.dorm_room_no'], ),
    sa.ForeignKeyConstraint(['faculty_id'], ['Faculty.faculty_id'], ),
    sa.PrimaryKeyConstraint('sid')
    )
    op.create_table('Tuition',
    sa.Column('tuition_semester', sa.Integer(), nullable=False),
    sa.Column('tuition_year', sa.Integer(), nullable=False),
    sa.Column('faculty_id', sa.Integer(), nullable=False),
    sa.Column('tuition_degree', sa.String(length=60), nullable=True),
    sa.Column('tuition_amount', sa.Integer(), nullable=True),
    sa.Column('tuition_start_date', sa.Date(), nullable=True),
    sa.Column('tuition_end_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['faculty_id'], ['Faculty.faculty_id'], ),
    sa.PrimaryKeyConstraint('tuition_semester', 'tuition_year', 'faculty_id')
    )
    op.create_table('Building_Room',
    sa.Column('room_no', sa.Integer(), nullable=False),
    sa.Column('building_name', sa.String(length=60), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['building_name'], ['Building.name'], ),
    sa.PrimaryKeyConstraint('room_no', 'building_name')
    )
    op.create_table('Pay_Tuition',
    sa.Column('sid', sa.Integer(), nullable=False),
    sa.Column('tuition_semester', sa.Integer(), nullable=False),
    sa.Column('tuition_year', sa.Integer(), nullable=False),
    sa.Column('faculty_id', sa.Integer(), nullable=False),
    sa.Column('tuition_late', sa.Boolean(), nullable=False),
    sa.Column('tuition_paid', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['faculty_id','tuition_semester','tuition_year'],\
       ['Tuition.faculty_id','Tuition.tuition_semester','Tuition.tuition_year'], ),
    sa.ForeignKeyConstraint(['sid'], ['Student.sid'], ),
    sa.PrimaryKeyConstraint('sid', 'tuition_semester', 'tuition_year', 'faculty_id')
    )
    op.create_table('Professor',
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.Column('major_id', sa.Integer(), nullable=True),
    sa.Column('faculty_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('surname', sa.String(length=60), nullable=False),
    sa.ForeignKeyConstraint(['faculty_id'], ['Major.faculty_id'], ),
    sa.ForeignKeyConstraint(['major_id'], ['Major.major_id'], ),
    sa.PrimaryKeyConstraint('professor_id')
    )
    op.create_table('Course',
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('section', sa.Integer(), nullable=False),
    sa.Column('course_semester_no', sa.Integer(), nullable=False),
    sa.Column('course_year', sa.Integer(), nullable=False),
    sa.Column('course_name', sa.String(length=60), nullable=False),
    sa.Column('credit', sa.Integer(), nullable=False),
    sa.Column('midterm_exam_date', sa.Date(), nullable=True),
    sa.Column('final_exam_date', sa.Date(), nullable=True),
    sa.Column('course_capacity', sa.Integer(), nullable=True),
    sa.Column('registered_amount', sa.Integer(), nullable=True),
    sa.Column('course_Type', sa.String(length=60), nullable=False),
    sa.Column('course_gpax', sa.Float(), nullable=True),
    sa.Column('major_id', sa.Integer(), nullable=True),
    sa.Column('faculty_id', sa.Integer(), nullable=True),
    sa.Column('room_no', sa.Integer(), nullable=True),
    sa.Column('building_name', sa.String(length=60), nullable=True),
    sa.ForeignKeyConstraint(['building_name','room_no'],\
     ['Building_Room.building_name','Building_Room.room_no'], ),
    sa.ForeignKeyConstraint(['course_semester_no','course_year'],\
     ['Semester.semester_no','Semester.year'], ),
    sa.ForeignKeyConstraint(['faculty_id','major_id'],\
     ['Major.faculty_id','Major.major_id'], ),
    sa.PrimaryKeyConstraint('course_id', 'section', 'course_semester_no', 'course_year')
    )
    op.create_table('Request',
    sa.Column('sid', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('section', sa.Integer(), nullable=False),
    sa.Column('course_semester_no', sa.Integer(), nullable=False),
    sa.Column('course_year', sa.Integer(), nullable=False),
    sa.Column('result', sa.String(length=60), nullable=True),
    sa.ForeignKeyConstraint(['course_id','section','course_semester_no','course_year'],\
     ['Course.course_id','Course.section','Course.course_semester_no','Course.course_year'], ),
    sa.ForeignKeyConstraint(['sid'], ['Student.sid'], ),
    sa.PrimaryKeyConstraint('sid', 'course_id', 'section', 'course_semester_no', 'course_year')
    )
    op.create_table('Study',
    sa.Column('sid', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('section', sa.Integer(), nullable=False),
    sa.Column('course_semester_no', sa.Integer(), nullable=False),
    sa.Column('course_year', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['course_id','section','course_semester_no','course_year'],\
     ['Course.course_id','Course.section','Course.course_semester_no','Course.course_year'], ),
    sa.ForeignKeyConstraint(['sid'], ['Student.sid'], ),
    sa.PrimaryKeyConstraint('sid', 'course_id', 'section', 'course_semester_no', 'course_year')
    )
    op.create_table('Teaches',
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('section', sa.Integer(), nullable=False),
    sa.Column('course_semester_no', sa.Integer(), nullable=False),
    sa.Column('course_year', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['professor_id'], ['Professor.professor_id'], ),
    sa.ForeignKeyConstraint(['course_id','section','course_semester_no','course_year'],\
     ['Course.course_id','Course.section','Course.course_semester_no','Course.course_year'], ),
    sa.PrimaryKeyConstraint('professor_id', 'course_id', 'section', 'course_semester_no', 'course_year')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Teaches')
    op.drop_table('Study')
    op.drop_table('Request')
    op.drop_table('Course')
    op.drop_table('Professor')
    op.drop_table('Pay_Tuition')
    op.drop_table('Building_Room')
    op.drop_table('Tuition')
    op.drop_table('Student')
    op.drop_table('Major')
    op.drop_table('Building')
    op.drop_table('Semester')
    op.drop_table('Faculty')
    op.drop_table('Dorm_Room')
    # ### end Alembic commands ###
