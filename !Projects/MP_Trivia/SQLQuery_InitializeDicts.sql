USE Trivia;
GO

INSERT INTO qDifficulties
			(DifficultyID, Difficulty)
     VALUES ('None', 'Mixed'),
			('easy', 'Easy'),
			('medium', 'Medium'),
			('hard', 'Hard');


INSERT INTO qTypes
			(TypeID, Type)
     VALUES ('None', 'Mixed'),
			('multiple', 'Multiple Choice'),
			('boolean', 'True/False ');
