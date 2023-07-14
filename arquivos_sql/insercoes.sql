INSERT INTO `departamentos` (`cod`, `Nome`) VALUES
(1, 'Departamento A'),
(2, 'Departamento B'),
(3, 'Departamento C');


INSERT INTO `professores` (`Nome`, `Email`, `Departamento_ID`) VALUES
('Prof. João', 'joao@example.com', 1),
('Prof. Maria', 'maria@example.com', 2),
('Prof. Carlos', 'carlos@example.com', 1);

INSERT INTO `disciplinas` (`cod`, `Nome`, `cod_departamento`) VALUES
('COD001', 'Matemática', 1),
('COD002', 'História', 2),
('COD003', 'Ciências', 1);

INSERT INTO `turmas` (`ID`, `periodo`, `professor`, `horario`, `local`, `cod_disciplina`, `cod_departamento`) VALUES
(1, '2023-01', 'Professor 1', 'Segunda-feira, 10:00-12:00', 'Sala A101', 'COD001', 1),
(2, '2023-01', 'Professor 2', 'Terça-feira, 14:00-16:00', 'Sala B202', 'COD002', 2),
(3, '2023-02', 'Professor 3', 'Quarta-feira, 8:00-10:00', 'Sala C303', 'COD003', 1);

INSERT INTO `estudantes` (`ID`, `Nome`, `Endereco`, `Email`, `Senha`, `matricula`, `Curso`, `is_admin`) VALUES
(1, 'João Silva', 'Rua A, 123', 'joao.silva@example.com', 'senha123', '20230001', 'Engenharia', 0),
(2, 'Maria Souza', 'Rua B, 456', 'maria.souza@example.com', 'senha456', '20230002', 'Medicina', 0),
(3, 'Pedro Santos', 'Rua C, 789', 'pedro.santos@example.com', 'senha789', '20230003', 'Direito', 1);

INSERT INTO `avaliacoes` (`ID`, `Estudante_ID`, `Turma_ID`, `Nota`, `Comentario`) VALUES
(1, 1, 1, 5, 'Ótima aula!'),
(2, 2, 2, 4, 'Interessante, mas difícil'),
(3, 3, 3, 3.5, 'Professor atencioso');


INSERT INTO `denuncias` (`Estudante_ID`, `avaliacao_ID`, `ocorrencias`) VALUES
(1, 1, 3),
(2, 2, 1),
(3, 3, 2);
