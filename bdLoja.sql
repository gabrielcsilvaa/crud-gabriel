create database loja ;

use loja;

create table produtos(
id int not null primary key,
nome varchar(50) not null,
preco float not null);

insert into produtos( id, nome, preco) values( 1, 'leite integral', 6.90);


alter table produtos modify id varchar(15);
ALTER TABLE produtos ADD imagem varchar(100);

update produtos
set imagem = 'https://acesse.dev/85RKt'
where id = "1";

update produtos
set id = 'LT01'
where id = "1";
