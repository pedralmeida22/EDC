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
