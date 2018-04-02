class Info:
    info_list = []

    def __init__(self,face_bookp,email_p):
        self.face_bookp =face_bookp
        self.email_p = email_p
    def save_info(self):
        Info.info_list.append(self)
    def delete_info(self):
        Info.info_list.remove(self)
    @classmethod
    def display_info(cls):
        return cls.info_list
