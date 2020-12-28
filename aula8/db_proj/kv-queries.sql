-- a
select nomes.value, mails.value
from Objects as nomes,
     Objects as mails
where
    nomes.id in (select id from Objects where key = "Tipo" and value = "Pessoa")
    and nomes.id in (select id from Objects where key = "Evento_ID")
    and nomes.id = mails.id
    and nomes.key = "Nome"
    and mails.key = "Email"

-- b
select events.value, locals.value
from Objects as events,
     Objects as elocal,
     Objects as locals
where
    events.id in (select id from Objects where key = "Tipo" and value = "Evento")
    and events.id = elocal.id
    and events.key = "Descricao"
    and elocal.key = "Local_ID"
    and locals.id in (select id from Objects where key = "Tipo" and value = "Local")
    and elocal.value in (locals.id)
    and locals.key = "Nome"

-- c
select events.value, locals.value
from Objects as events,
     Objects as elocal,
     Objects as locals
where
    events.id in (select id from Objects where key = "Tipo" and value = "Evento")
    and events.id = elocal.id
    and events.key = "Descricao"
    and elocal.key = "Local_ID"
    and locals.id = "l2"    -- substituir por local pretendido
    and elocal.value in (locals.id)
    and locals.key = "Nome";

-- d
select desc.value
from Objects as desc,
     Objects as time
where
    desc.id in (select id from Objects where key = "Tipo" and value = "Evento")
    and desc.id = time.id
    and time.key = "Inicio"
    and time.value = "10:00"
    and desc.key = "Descricao"

-- e
select nomes.value, mails.value
from Objects as nomes,
     Objects as mails,
     Objects as events
where
    nomes.id in (select id from Objects where key = "Tipo" and value = "Pessoa")
    and nomes.id in (select id from Objects where key = "Evento_ID")
    and mails.id = nomes.id
    and events.id = nomes.id
    and nomes.key = "Nome"
    and mails.key = "Email"
    and events.key = "Evento_ID"
    and events.value = "e2"
