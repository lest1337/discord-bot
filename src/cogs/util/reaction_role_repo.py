import src.db.database as db

class ReactionRoleRepo:

    def add_message(self, message_id: int, emoji: str, role_id: int):
        with db.get_connexion() as conn:
            conn.execute("""
insert into reaction_role (message_id, role_id, emoji)
values (?, ?, ?)
""", (message_id, role_id, emoji))
            conn.commit()
            
    def remove_message(self, message_id: int):
        with db.get_connexion() as conn:
            conn.execute("""
delete from reaction_role where message_id = ?
""", (message_id,))
            conn.commit()
            
    def get_message(self, message_id: int):
        with db.get_connexion() as conn:
            return conn.execute("""
select * from reaction_role where message_id = ?;
""", (message_id,)).fetchall()