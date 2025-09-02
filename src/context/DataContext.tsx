import React, { createContext, useContext, useState, useEffect } from 'react';
import Papa from 'papaparse';
import { Student, Group, Exam, ExamGrade, Absence, Lesson } from '../types';

interface DataContextType {
  students: Student[];
  groups: Group[];
  exams: Exam[];
  examGrades: ExamGrade[];
  absences: Absence[];
  lessons: Lesson[];
  loading: boolean;
  error: string | null;
  refreshData: () => void;
}

const DataContext = createContext<DataContextType | undefined>(undefined);

export const useData = () => {
  const context = useContext(DataContext);
  if (context === undefined) {
    throw new Error('useData must be used within a DataProvider');
  }
  return context;
};

export const DataProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [students, setStudents] = useState<Student[]>([]);
  const [groups, setGroups] = useState<Group[]>([]);
  const [exams, setExams] = useState<Exam[]>([]);
  const [examGrades, setExamGrades] = useState<ExamGrade[]>([]);
  const [absences, setAbsences] = useState<Absence[]>([]);
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const loadCSVFile = async <T,>(filename: string): Promise<T[]> => {
    try {
      const response = await fetch(`/${filename}`);
      if (!response.ok) {
        throw new Error(`Failed to load ${filename}`);
      }
      const csvText = await response.text();
      
      return new Promise((resolve, reject) => {
        Papa.parse(csvText, {
          header: true,
          delimiter: ';',
          skipEmptyLines: true,
          complete: (results) => {
            if (results.errors.length > 0) {
              reject(new Error(`Error parsing ${filename}: ${results.errors[0].message}`));
            } else {
              resolve(results.data as T[]);
            }
          },
          error: (error) => {
            reject(new Error(`Error parsing ${filename}: ${error.message}`));
          }
        });
      });
    } catch (err) {
      throw new Error(`Failed to load ${filename}: ${err instanceof Error ? err.message : 'Unknown error'}`);
    }
  };

  const loadData = async () => {
    setLoading(true);
    setError(null);
    
    try {
      const [
        studentsData,
        groupsData,
        examsData,
        examGradesData,
        absencesData,
        lessonsData
      ] = await Promise.all([
        loadCSVFile<Student>('students.csv'),
        loadCSVFile<Group>('groups.csv'),
        loadCSVFile<Exam>('exams.csv'),
        loadCSVFile<ExamGrade>('exam_grades.csv'),
        loadCSVFile<Absence>('absences.csv'),
        loadCSVFile<Lesson>('lessons.csv')
      ]);

      setStudents(studentsData);
      setGroups(groupsData);
      setExams(examsData);
      setExamGrades(examGradesData);
      setAbsences(absencesData);
      setLessons(lessonsData);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'حدث خطأ في تحميل البيانات');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  const refreshData = () => {
    loadData();
  };

  return (
    <DataContext.Provider value={{
      students,
      groups,
      exams,
      examGrades,
      absences,
      lessons,
      loading,
      error,
      refreshData
    }}>
      {children}
    </DataContext.Provider>
  );
};