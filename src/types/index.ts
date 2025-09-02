export interface Student {
  الاسم: string;
  الصف: string;
  البريد: string;
  المجموعة: string;
  الهاتف: string;
}

export interface Group {
  المجموعة: string;
  الصف: string;
}

export interface Exam {
  اسم_الامتحان: string;
  الدرجة_الكلية: number;
  التاريخ: string;
  الوصف: string;
  الصف: string;
  الحالة: string;
}

export interface ExamGrade {
  اسم_الامتحان: string;
  اسم_الطالب: string;
  الدرجة: number;
}

export interface Absence {
  الاسم: string;
  المجموعة: string;
  الحصة: string;
  التاريخ: string;
  الحالة: string;
  الهاتف: string;
}

export interface Lesson {
  الحصة: string;
  الوقت: string;
  الوصف: string;
}