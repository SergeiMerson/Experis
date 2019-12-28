USE Trivia;
GO


DROP VIEW IF EXISTS View_Questions;
GO


CREATE VIEW View_Questions AS
SELECT  q.QuestionID,
		qcat.Category,
		qdif.Difficulty,
		qtype.Type,
		q.Question
  FROM  Questions AS q
  JOIN  qCategories AS qcat
    ON  q.CategoryID = qcat.CategoryID
  JOIN  qDifficulties AS qdif
    ON  q.DifficultyID = qdif.DifficultyID
  JOIN  qTypes AS qtype
    ON  q.TypeID = qtype.TypeID