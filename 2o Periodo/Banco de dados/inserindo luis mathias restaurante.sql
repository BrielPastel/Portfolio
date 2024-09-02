USE restaurante;

CREATE VIEW produtos_por_clientes(cliente_id, cliente_nome, data_nascimento, data_criacao, produto_id, produto_nome, quantidade) AS
SELECT c.id, p.nome, p.data_nasc, c.data_criacao,
pr.id, pr.nome, SUM(r.quantidade)
FROM pessoa AS p
INNER JOIN cliente AS c ON p.id = c.id
INNER JOIN comanda AS cm ON cm.id_cliente = c.id
INNER JOIN registro AS r ON r.id_comanda = cm.id
LEFT JOIN produto AS pr ON r.id_produto = pr.id
GROUP BY p.id, pr.id
ORDER BY SUM(r.quantidade) DESC;

SELECT * FROM produtos_por_clientes;

SELECT cliente_nome, SUM(quantidade) FROM produtos_por_clientes GROUP BY cliente_nome;


DELIMITER $$
CREATE PROCEDURE insert_lm (IN _nome VARCHAR(200), IN _cpf CHAR(11), IN _sexo CHAR(11), IN _data_nasc DATE)
BEGIN
	INSERT INTO pessoa
    VALUES(NULL, _nome, _cpf, _sexo, _data_nasc);
    INSERT INTO cliente
    VALUES(last_insert_id(), now());
    INSERT INTO comanda
    VALUES(NULL, now(), 0.0, 0, last_insert_id(), NULL);
    SELECT last_insert_id();

END $$

DELIMITER ;

CALL insert_lm('Luís Mathias', '19245239285', 'M', '2005-04-10');
DROP PROCEDURE insert_lm;

SELECT * FROM pessoa;