create table if not exists reaction_role(
    message_id integer not null,
    role_id integer not null,
    emoji text not null
);