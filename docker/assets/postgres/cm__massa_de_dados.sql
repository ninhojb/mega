
--------------------
-- CM

INSERT INTO cm.grupo_controle_campanha
(gc, tipo_grupo_controle, grupo_controle, id_campanha, id_regua_interacao, criado_em, alterado_em, idx_percentual, ativo)
VALUES
(0, 'CANAL', 'TODOS CANAIS', 1, NULL, current_timestamp, NULL, 0.2, true),
(1, 'CANAL', 'NENHUM CANAL', 1, NULL, current_timestamp, NULL, 0.2, true),
(2, 'CANAL', 'CANAL EMAIL', 1, NULL, current_timestamp, NULL, 0.2, true),
(3, 'CANAL', 'CANAL SMS', 1, NULL, current_timestamp, NULL, 0.2, true),
(4, 'CANAL', 'CANAL DISCADOR', 1, NULL, current_timestamp, NULL, 0.2, true)
;