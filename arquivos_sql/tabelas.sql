CREATE TABLE `departamentos` (
  `cod` int NOT NULL,
  `Nome` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `professores` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Departamento_ID` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Departamento_ID` (`Departamento_ID`),
  CONSTRAINT `professores_ibfk_1` FOREIGN KEY (`Departamento_ID`) REFERENCES `departamentos` (`cod`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `disciplinas` (
  `cod` varchar(255) NOT NULL,
  `Nome` varchar(255) DEFAULT NULL,
  `cod_departamento` int DEFAULT NULL,
  PRIMARY KEY (`cod`),
  KEY `cod_departamento` (`cod_departamento`),
  CONSTRAINT `disciplinas_ibfk_1` FOREIGN KEY (`cod_departamento`) REFERENCES `departamentos` (`cod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `turmas` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `periodo` varchar(255) DEFAULT NULL,
  `professor` varchar(255) DEFAULT NULL,
  `horario` varchar(255) DEFAULT NULL,
  `local` varchar(255) DEFAULT NULL,
  `cod_disciplina` varchar(255) DEFAULT NULL,
  `cod_departamento` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `cod_disciplina` (`cod_disciplina`),
  KEY `cod_departamento` (`cod_departamento`),
  CONSTRAINT `turmas_ibfk_1` FOREIGN KEY (`cod_disciplina`) REFERENCES `disciplinas` (`cod`),
  CONSTRAINT `turmas_ibfk_2` FOREIGN KEY (`cod_departamento`) REFERENCES `departamentos` (`cod`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `estudantes` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(255) DEFAULT NULL,
  `Endereco` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Senha` varchar(255) DEFAULT NULL,
  `matricula` varchar(10) DEFAULT NULL,
  `Curso` varchar(20) DEFAULT NULL,
  `foto` longblob,
  `is_admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `avaliacoes` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Estudante_ID` int DEFAULT NULL,
  `Turma_ID` int DEFAULT NULL,
  `Nota` decimal(5,2) DEFAULT NULL,
  `Comentario` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Estudante_ID` (`Estudante_ID`),
  KEY `Turma_ID` (`Turma_ID`),
  CONSTRAINT `avaliacoes_ibfk_1` FOREIGN KEY (`Estudante_ID`) REFERENCES `estudantes` (`ID`),
  CONSTRAINT `avaliacoes_ibfk_2` FOREIGN KEY (`Turma_ID`) REFERENCES `turmas` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `denuncias` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Estudante_ID` int DEFAULT NULL,
  `avaliacao_ID` int DEFAULT NULL,
  `ocorrencias` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Estudante_ID` (`Estudante_ID`),
  KEY `fk_avaliacao_denuncia` (`avaliacao_ID`),
  CONSTRAINT `denuncias_ibfk_1` FOREIGN KEY (`Estudante_ID`) REFERENCES `estudantes` (`ID`),
  CONSTRAINT `fk_avaliacao_denuncia` FOREIGN KEY (`avaliacao_ID`) REFERENCES `avaliacoes` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `maioresavaliacoes` AS select `t`.`professor` AS `professor`,`dis`.`Nome` AS `Nome`,avg(`a`.`Nota`) AS `media_avaliacao`,`t`.`cod_disciplina` AS `cod_disciplina` from ((`turmas` `t` left join `avaliacoes` `a` on((`t`.`ID` = `a`.`Turma_ID`))) left join `disciplinas` `dis` on((`t`.`cod_disciplina` = `dis`.`cod`))) group by `t`.`professor`,`dis`.`Nome`,`t`.`cod_disciplina` order by `media_avaliacao` desc limit 5;


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `apagar_comentario_denunciado`(IN p_comentario_id INT)
BEGIN
    -- Deletar a denúncia relacionada ao comentário
    DELETE FROM denuncias WHERE avaliacao_ID = p_comentario_id;
    
    -- Deletar o comentário
    DELETE FROM avaliacoes WHERE ID = p_comentario_id;
END$$
DELIMITER ;
