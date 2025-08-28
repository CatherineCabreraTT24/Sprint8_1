-- Crear tabla Employee
CREATE TABLE Clientes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Age INTEGER,
    Country TEXT
);

-- Insertar algunos registros de ejemplo
INSERT INTO Clientes (Name, Age, Country) VALUES
('Juan Pérez', 28, 'Colombia'),
('Ana Gómez', 22, 'México'),
('José Ramírez', 35, 'Colombia'),
('María López', 30, 'Argentina'),
('John Smith', 40, 'USA'),
('Juliana Torres', 27, 'Colombia'),
('Pedro Sánchez', 24, 'Chile');