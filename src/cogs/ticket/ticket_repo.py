import src.db.database as db

class TicketRepo:
    def __init__(self) -> None:
        self.conn = db.get_connexion()

    # Getters
    def get_ticket_channel(self, channel_id: int):
        return self.conn.execute(f"""
select * from ticket where channel_id = {channel_id}
""").fetchone()
    
    def get_ticket_from_user(self, user_id: int):
        return self.conn.execute(f"""
select * from ticket where user_id = {user_id};
""").fetchone()
    
    def get_ticket_message(self):
        return self.conn.execute(f"""
select * from ticket_message;
""").fetchall()

    # Setters
    def add_ticket_message(self, message_id: int):
        self.conn.execute(f"""
insert into ticket_message (message_id)
values ({message_id});
""")

    def add_ticket_channel(self, user_id: int, channel_id: int):
        self.conn.execute(f"""
insert into ticket (user_id, channel_id)
values ({user_id}, {channel_id});
""")
        
    def remove_ticket_channel(self, channel_id: int):
        self.conn.execute(f"""
delete from ticket
where channel_id = {channel_id};
""")