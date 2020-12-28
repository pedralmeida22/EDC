-- a
SELECT *
FROM Pessoa JOIN Evento E on E.ID = Pessoa.Evento_ID;

-- a alternative
SELECT *
FROM Pessoa
WHERE Evento_ID is not NULL;

-- b
SELECT Evento.Descricao, L.Nome
FROM Evento JOIN Local L on L.ID = Evento.Local_ID;

-- c
SELECT Evento.Descricao, L.Nome
FROM Evento JOIN Local L on L.ID = Evento.Local_ID
WHERE L.ID = "l1";

-- d
SELECT Descricao
FROM Evento
where Inicio = "09:00";

-- e
SELECT Pessoa.Nome, Pessoa.Email
from Pessoa join Evento E on E.ID = Pessoa.Evento_ID
where e.ID = "e2"

-- f
SELECT Pessoa.Nome, Pessoa.Email
from Pessoa join Evento E on E.ID = Pessoa.Evento_ID join Local L on L.ID = E.Local_ID
where e.ID = "e1" and L.ID = "l1"