import React, { useState } from 'react';
import { FileText, Plus, Calendar, Award, BarChart3 } from 'lucide-react';
import { useData } from '../context/DataContext';

export const ExamsView: React.FC = () => {
  const { exams, examGrades, loading } = useData();
  const [selectedExam, setSelectedExam] = useState<string>('');

  const getExamStats = (examName: string) => {
    const grades = examGrades.filter(grade => grade.اسم_الامتحان === examName);
    if (grades.length === 0) return { average: 0, highest: 0, lowest: 0, total: 0 };
    
    const scores = grades.map(g => g.الدرجة);
    return {
      average: scores.reduce((a, b) => a + b, 0) / scores.length,
      highest: Math.max(...scores),
      lowest: Math.min(...scores),
      total: scores.length
    };
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">إدارة الامتحانات</h1>
          <p className="text-gray-600">متابعة الامتحانات والدرجات</p>
        </div>
        <button className="btn-primary flex items-center gap-2">
          <Plus className="w-5 h-5" />
          إنشاء امتحان جديد
        </button>
      </div>

      {/* Exams Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {exams.map((exam, index) => {
          const stats = getExamStats(exam.اسم_الامتحان);
          const isSelected = selectedExam === exam.اسم_الامتحان;
          
          return (
            <div 
              key={index} 
              className={`card cursor-pointer transition-all duration-200 ${
                isSelected ? 'ring-2 ring-primary-500 shadow-lg' : 'hover:shadow-lg'
              }`}
              onClick={() => setSelectedExam(isSelected ? '' : exam.اسم_الامتحان)}
            >
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-center gap-3">
                  <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center">
                    <FileText className="w-6 h-6 text-primary-600" />
                  </div>
                  <div>
                    <h3 className="text-lg font-bold text-gray-900">{exam.اسم_الامتحان}</h3>
                    <p className="text-sm text-gray-600">{exam.الوصف}</p>
                  </div>
                </div>
                <span className={`status-badge ${
                  exam.الحالة === 'مفتوح' ? 'status-present' : 'bg-gray-100 text-gray-800'
                }`}>
                  {exam.الحالة}
                </span>
              </div>

              <div className="grid grid-cols-2 gap-4 mb-4">
                <div className="text-center p-3 bg-gray-50 rounded-lg">
                  <p className="text-2xl font-bold text-gray-900">{exam.الدرجة_الكلية}</p>
                  <p className="text-xs text-gray-600">الدرجة الكلية</p>
                </div>
                <div className="text-center p-3 bg-gray-50 rounded-lg">
                  <p className="text-2xl font-bold text-gray-900">{stats.total}</p>
                  <p className="text-xs text-gray-600">عدد الطلاب</p>
                </div>
              </div>

              <div className="flex items-center justify-between text-sm text-gray-600">
                <div className="flex items-center gap-2">
                  <Calendar className="w-4 h-4" />
                  {new Date(exam.التاريخ).toLocaleDateString('ar-EG')}
                </div>
                <div className="flex items-center gap-2">
                  <Award className="w-4 h-4" />
                  متوسط: {stats.average.toFixed(1)}
                </div>
              </div>

              {isSelected && stats.total > 0 && (
                <div className="mt-4 pt-4 border-t border-gray-200 animate-slide-up">
                  <h4 className="font-semibold text-gray-900 mb-3 flex items-center gap-2">
                    <BarChart3 className="w-4 h-4" />
                    إحصائيات الامتحان
                  </h4>
                  <div className="grid grid-cols-3 gap-3 text-center">
                    <div className="p-2 bg-success-50 rounded-lg">
                      <p className="text-lg font-bold text-success-700">{stats.highest}</p>
                      <p className="text-xs text-success-600">أعلى درجة</p>
                    </div>
                    <div className="p-2 bg-warning-50 rounded-lg">
                      <p className="text-lg font-bold text-warning-700">{stats.average.toFixed(1)}</p>
                      <p className="text-xs text-warning-600">المتوسط</p>
                    </div>
                    <div className="p-2 bg-error-50 rounded-lg">
                      <p className="text-lg font-bold text-error-700">{stats.lowest}</p>
                      <p className="text-xs text-error-600">أقل درجة</p>
                    </div>
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>

      {exams.length === 0 && (
        <div className="card text-center py-12">
          <FileText className="w-16 h-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-xl font-semibold text-gray-900 mb-2">لا توجد امتحانات</h3>
          <p className="text-gray-600 mb-6">ابدأ بإنشاء امتحان جديد لطلابك</p>
          <button className="btn-primary flex items-center gap-2 mx-auto">
            <Plus className="w-5 h-5" />
            إنشاء امتحان جديد
          </button>
        </div>
      )}
    </div>
  );
};