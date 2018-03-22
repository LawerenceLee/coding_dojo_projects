class FormValidation(object):
    def __init__(self, form):
        self.course_name = form["name"]
        self.description = form['desc']
        self.errors = []

        self.is_course_description_valid()
        self.is_course_name_valid()
    
    def is_course_name_valid(self):
        if len(self.course_name) <= 5:
            self.errors.append(
                "Course Name must be longer than 5 characters"
            )

    def is_course_description_valid(self):
        if len(self.description) <= 15:
            self.errors.append(
                "Course Description must be more than 15 characters."
            )
