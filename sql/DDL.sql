-- SQL Star Schema Sample -- Admissions Table
CREATE TABLE Admissions (
    AdmissionID INT PRIMARY KEY,
    PatientID INT,
    AdmissionDate DATE,
    DiagnosisCode VARCHAR(20),
    HospitalID INT
);

-- Aggregate Table
CREATE TABLE AdmissionsAgg (
    DiagnosisCode VARCHAR(20),
    AdmissionsCount INT
);

-- Example query: Admissions by Diagnosis
SELECT DiagnosisCode, COUNT(*) FROM Admissions GROUP BY DiagnosisCode;