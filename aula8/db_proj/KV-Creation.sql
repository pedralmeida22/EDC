CREATE TABLE Objects
(
  id        TEXT,
  key       TEXT,
  value     TEXT
);

INSERT INTO Objects VALUES('l1', 'Tipo', 'Local');
INSERT INTO Objects VALUES('l1', 'Nome', 'UA');
INSERT INTO Objects VALUES('l1', 'Descricao', 'Universidade de Aveiro');

INSERT INTO Objects VALUES('l2', 'Tipo', 'Local');
INSERT INTO Objects VALUES('l2', 'Nome', 'UC');
INSERT INTO Objects VALUES('l2', 'Descricao', 'Universidade de Coimbra');

INSERT INTO Objects VALUES('l3', 'Tipo', 'Local');
INSERT INTO Objects VALUES('l3', 'Nome', 'UP');
INSERT INTO Objects VALUES('l3', 'Descricao', 'Universidade do Porto');

INSERT INTO Objects VALUES('l4', 'Tipo', 'Local');
INSERT INTO Objects VALUES('l4', 'Nome', 'UL');
INSERT INTO Objects VALUES('l4', 'Descricao', 'Universidade de Lisboa');



INSERT INTO Objects VALUES('e1', 'Tipo', 'Evento');
INSERT INTO Objects VALUES('e1', 'Nome', 'Abertura UA');
INSERT INTO Objects VALUES('e1', 'Descricao', 'Festa comemorativa da abertura do ano letivo na Universidade de Aveiro');
INSERT INTO Objects VALUES('e1', 'Data', '2017-09-20');
INSERT INTO Objects VALUES('e1', 'Inicio', '09:00');
INSERT INTO Objects VALUES('e1', 'Fim', '18:00');
INSERT INTO Objects VALUES('e1', 'Local_ID', 'l1');

INSERT INTO Objects VALUES('e2', 'Tipo', 'Evento');
INSERT INTO Objects VALUES('e2', 'Nome', 'Abertura UA');
INSERT INTO Objects VALUES('e2', 'Descricao', 'Festa comemorativa da abertura do ano letivo na Universidade de Coimbra');
INSERT INTO Objects VALUES('e2', 'Data', '2017-09-30');
INSERT INTO Objects VALUES('e2', 'Inicio', '10:00');
INSERT INTO Objects VALUES('e2', 'Fim', '19:00');
INSERT INTO Objects VALUES('e2', 'Local_ID', 'l2');

INSERT INTO Objects VALUES('e3', 'Tipo', 'Evento');
INSERT INTO Objects VALUES('e3', 'Nome', 'Abertura UA');
INSERT INTO Objects VALUES('e3', 'Descricao', 'Festa comemorativa da abertura do ano letivo na Universidade do Porto');
INSERT INTO Objects VALUES('e3', 'Data', '2017-09-25');
INSERT INTO Objects VALUES('e3', 'Inicio', '13:00');
INSERT INTO Objects VALUES('e3', 'Fim', '20:00');
INSERT INTO Objects VALUES('e3', 'Local_ID', 'l3');

INSERT INTO Objects VALUES('e4', 'Tipo', 'Evento');
INSERT INTO Objects VALUES('e4', 'Nome', 'Abertura UA');
INSERT INTO Objects VALUES('e4', 'Descricao', 'Festa comemorativa da abertura do ano letivo na Universidade de Lisboa');
INSERT INTO Objects VALUES('e4', 'Data', '2017-09-27');
INSERT INTO Objects VALUES('e4', 'Inicio', '15:00');
INSERT INTO Objects VALUES('e4', 'Fim', '23:00');
INSERT INTO Objects VALUES('e4', 'Local_ID', 'l4');



INSERT INTO Objects VALUES('p1', 'Tipo', 'Pessoa');
INSERT INTO Objects VALUES('p1', 'Nome', 'João');
INSERT INTO Objects VALUES('p1', 'Email', 'joao@ua.pt');
INSERT INTO Objects VALUES('p1', 'Evento_ID', 'e1');

INSERT INTO Objects VALUES('p2', 'Tipo', 'Pessoa');
INSERT INTO Objects VALUES('p2', 'Nome', 'José');
INSERT INTO Objects VALUES('p2', 'Email', 'jose@uc.pt');
INSERT INTO Objects VALUES('p2', 'Evento_ID', 'e2');

INSERT INTO Objects VALUES('p3', 'Tipo', 'Pessoa');
INSERT INTO Objects VALUES('p3', 'Nome', 'Manuel');
INSERT INTO Objects VALUES('p3', 'Email', 'manuel@up.pt');
INSERT INTO Objects VALUES('p3', 'Evento_ID', 'e3');

INSERT INTO Objects VALUES('p4', 'Tipo', 'Pessoa');
INSERT INTO Objects VALUES('p4', 'Nome', 'Joaquim');
INSERT INTO Objects VALUES('p4', 'Email', 'joaquim@ul.pt');
INSERT INTO Objects VALUES('p4', 'Evento_ID', 'e4');

INSERT INTO Objects VALUES('p5', 'Tipo', 'Pessoa');
INSERT INTO Objects VALUES('p5', 'Nome', 'Antonio');
INSERT INTO Objects VALUES('p5', 'Email', 'antonio@ua.pt');
INSERT INTO Objects VALUES('p5', 'Evento_ID', NULL); -- nao criar esta entrada

