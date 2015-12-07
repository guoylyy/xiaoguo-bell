from app import db

class Bell(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    create_time = db.Column(db.Date)
    
    update_time = db.Column(db.Date)
    
    request_time = db.Column(db.Date)
    
    is_played = db.Column(db.Boolean)
    
    repeat_times = db.Column(db.Integer)
    

    def to_dict(self):
        return dict(
            create_time = self.create_time.isoformat(),
            update_time = self.update_time.isoformat(),
            request_time = self.request_time.isoformat(),
            is_played = self.is_played,
            repeat_times = self.repeat_times,
            id = self.id
        )

    def __repr__(self):
        return '<Bell %r>' % (self.id)
