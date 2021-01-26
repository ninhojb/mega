
--------------------
-- RAW

INSERT INTO raw.clientes
(codigo, nome, cpf, endereco, numero,fone, dta_nascimento, e_mail, dta_cad)
VALUES(1, 'Renato Brandao', '43153794840', 'rua 1', '1', '11944616283', '11/01/1987', 'renato.brandao@aldata.io','01/01/2010')
;

INSERT INTO raw.clientes
(codigo, nome, cpf, endereco, numero,fone, dta_nascimento, e_mail, dta_cad)
VALUES(2, 'Aline Franca', '43153794840', 'rua 2', '2', '11974221155', '11/01/1965', 'aline.franca@aldata.io','01/01/2011')
;

INSERT INTO raw.clientes
(codigo, nome, cpf, endereco, numero,fone, dta_nascimento, e_mail, dta_cad)
VALUES(3, 'Paulo Henrique Cavaretto ', '43153794840', 'rua 3', '3', '11997966402', '11/01/1987', 'paulo.cavaretto@aldata.io','01/01/2010')
;

INSERT INTO raw.clientes
(codigo, nome, cpf, endereco, numero,fone, dta_nascimento, e_mail, dta_cad)
VALUES(4, 'Raphael Costa', '43153794840', 'rua 4', '4', '11980225927', '01/01/1960', 'raocosta@gmail.com','01/01/2011')
;

INSERT INTO raw.clientes
(codigo, nome, cpf, endereco, numero,fone, dta_nascimento, e_mail, dta_cad)
VALUES(5, 'Ned Borges', '43153794840', 'rua 5', '5', '11954581526', '01/01/1990', 'ninhojb@bol.com.br','01/01/2015')
;

INSERT INTO raw.clientes
(codigo, nome, cpf, endereco, numero,fone, dta_nascimento, e_mail, dta_cad)
VALUES(6, 'Ned sem mail', '43153794840', 'rua 6', '6', '11954581526', '11/01/1987', '','01/01/2010')
;

INSERT INTO raw.clientes
(codigo, nome, cpf, endereco, numero,fone, dta_nascimento, e_mail, dta_cad)
VALUES(7, 'Ned errado', '43153794840', 'rua 7', '7', '11954581526', '11/01/1987', '','01/01/2010')
;

INSERT INTO raw.clientes
(codigo, nome, cpf, endereco, numero,fone, dta_nascimento, e_mail, dta_cad)
VALUES(8, 'Ned sem numero', '43153794840', 'rua 6', '6', '', '11/01/1987', 'ninhojb@gmail.com','01/01/2010')
;

INSERT INTO raw.bancos
(codigo, nome)
VALUES(1000, 'Escola Infantil')
;

INSERT INTO raw.bancos
(codigo, nome)
VALUES(2000, 'Escola Estadual')
;

INSERT INTO raw.bancos
(codigo, nome)
VALUES(3000, 'Escola Governamental')
;

INSERT INTO raw.operacoes
(cliente, nroperacao, remessa, banco,  valordivida, dias_atrazo)
VALUES(1, '1234', 100,1000 ,187,50)
;

INSERT INTO raw.operacoes
(cliente, nroperacao, remessa, banco,  valordivida, dias_atrazo)
VALUES(2, '120', 548,2000 ,578,40)
;

INSERT INTO raw.operacoes
(cliente, nroperacao, remessa, banco,  valordivida, dias_atrazo)
VALUES(3, '1234', 14,3000 ,87,90)
;

INSERT INTO raw.operacoes
(cliente, nroperacao, remessa, banco,  valordivida, dias_atrazo)
VALUES(4, '134', 10,1000 ,17,10)
;

INSERT INTO raw.operacoes
(cliente, nroperacao, remessa, banco,  valordivida, dias_atrazo)
VALUES(5, '234', 150,2000 ,87,60)
;

INSERT INTO raw.operacoes
(cliente, nroperacao, remessa, banco,  valordivida, dias_atrazo)
VALUES(6, '1234', 100,3000 ,17,10)
;

INSERT INTO raw.operacoes
(cliente, nroperacao, remessa, banco,  valordivida, dias_atrazo)
VALUES(7, '1234', 20,3000 ,17,10)
;

INSERT INTO raw.operacoes
(cliente, nroperacao, remessa, banco,  valordivida, dias_atrazo)
VALUES(8, '1234', 100, 3000 ,17,10)
;


------------------------------------
