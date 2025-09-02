import React from 'react';
import { Calendar, Award, AlertCircle } from 'lucide-react';
import { Absence, ExamGrade } from '../types';

interface RecentActivityProps {
  recentAbsences: Absence[];
  recentGrades: ExamGrade[];
}

export const RecentActivity: React.FC<RecentActivityProps> = ({ 
  recentAbsences, 
  recentGrades 
}) => {
  return (
    <div className="card">
      <div className="flex items-center gap-3 mb-6">
        <Calendar className="w-6 h-6 text-primary-600" />
        <h2 className="text-xl font-bold text-gray-900">النشاط الأخير</h2>
      </div>

      <div className="space-y-4">
        {/* Recent Absences */}
        <div>
          <h3 className="text-lg font-semibold text-gray-800 mb-3 flex items-center gap-2">
            <AlertCircle className="w-5 h-5 text-warning-600" />
            حالات الغياب الأخيرة
          </h3>
          <div className="space-y-2">
            {recentAbsences.length > 0 ? (
              recentAbsences.map((absence, index) => (
                <div key={index} className="flex items-center justify-between p-3 bg-warning-50 rounded-lg border border-warning-100">
                  <div>
                    <p className="font-medium text-gray-900">{absence.الاسم}</p>
                    <p className="text-sm text-gray-600">{absence.المجموعة} - {absence.الحصة}</p>
                  </div>
                  <span className="text-sm text-warning-700 font-medium">
                    {new Date(absence.التاريخ).toLocaleDateString('ar-EG')}
                  </span>
                </div>
              ))
            ) : (
              <p className="text-gray-500 text-center py-4">لا توجد حالات غياب حديثة</p>
            )}
          </div>
        </div>

        {/* Recent Grades */}
        <div>
          <h3 className="text-lg font-semibold text-gray-800 mb-3 flex items-center gap-2">
            <Award className="w-5 h-5 text-success-600" />
            الدرجات الأخيرة
          </h3>
          <div className="space-y-2">
            {recentGrades.length > 0 ? (
              recentGrades.map((grade, index) => (
                <div key={index} className="flex items-center justify-between p-3 bg-success-50 rounded-lg border border-success-100">
                  <div>
                    <p className="font-medium text-gray-900">{grade.اسم_الطالب}</p>
                    <p className="text-sm text-gray-600">{grade.اسم_الامتحان}</p>
                  </div>
                  <span className="text-lg font-bold text-success-700">
                    {grade.الدرجة}
                  </span>
                </div>
              ))
            ) : (
              <p className="text-gray-500 text-center py-4">لا توجد درجات حديثة</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};