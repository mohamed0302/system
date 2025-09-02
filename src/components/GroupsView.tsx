import React from 'react';
import { Users, Plus, GraduationCap } from 'lucide-react';
import { useData } from '../context/DataContext';

export const GroupsView: React.FC = () => {
  const { groups, students, loading } = useData();

  const getGroupStats = (groupName: string) => {
    const groupStudents = students.filter(student => student.المجموعة === groupName);
    return {
      studentCount: groupStudents.length,
      students: groupStudents
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
          <h1 className="text-2xl font-bold text-gray-900">إدارة المجموعات</h1>
          <p className="text-gray-600">تنظيم الطلاب في مجموعات دراسية</p>
        </div>
        <button className="btn-primary flex items-center gap-2">
          <Plus className="w-5 h-5" />
          إنشاء مجموعة جديدة
        </button>
      </div>

      {/* Groups Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {groups.map((group, index) => {
          const stats = getGroupStats(group.المجموعة);
          
          return (
            <div key={index} className="card hover:shadow-lg transition-all duration-200 group">
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-3">
                  <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center group-hover:bg-primary-200 transition-colors duration-200">
                    <Users className="w-6 h-6 text-primary-600" />
                  </div>
                  <div>
                    <h3 className="text-lg font-bold text-gray-900">{group.المجموعة}</h3>
                    <p className="text-sm text-gray-600 flex items-center gap-1">
                      <GraduationCap className="w-4 h-4" />
                      {group.الصف}
                    </p>
                  </div>
                </div>
              </div>

              <div className="bg-gray-50 rounded-lg p-4 mb-4">
                <div className="flex items-center justify-between">
                  <span className="text-sm text-gray-600">عدد الطلاب</span>
                  <span className="text-2xl font-bold text-gray-900">{stats.studentCount}</span>
                </div>
              </div>

              {stats.students.length > 0 && (
                <div className="space-y-2">
                  <h4 className="text-sm font-semibold text-gray-700 mb-2">الطلاب:</h4>
                  <div className="max-h-32 overflow-y-auto space-y-1">
                    {stats.students.map((student, studentIndex) => (
                      <div key={studentIndex} className="flex items-center gap-2 p-2 bg-gray-50 rounded-lg">
                        <div className="w-6 h-6 bg-primary-100 rounded-full flex items-center justify-center">
                          <span className="text-primary-700 font-semibold text-xs">
                            {student.الاسم.charAt(0)}
                          </span>
                        </div>
                        <span className="text-sm text-gray-900">{student.الاسم}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              <div className="mt-4 pt-4 border-t border-gray-200">
                <div className="flex gap-2">
                  <button className="flex-1 text-primary-600 hover:text-primary-800 text-sm font-medium transition-colors duration-200">
                    عرض التفاصيل
                  </button>
                  <button className="flex-1 text-gray-600 hover:text-gray-800 text-sm font-medium transition-colors duration-200">
                    تعديل
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {groups.length === 0 && (
        <div className="card text-center py-12">
          <Users className="w-16 h-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-xl font-semibold text-gray-900 mb-2">لا توجد مجموعات</h3>
          <p className="text-gray-600 mb-6">ابدأ بإنشاء مجموعة دراسية جديدة</p>
          <button className="btn-primary flex items-center gap-2 mx-auto">
            <Plus className="w-5 h-5" />
            إنشاء مجموعة جديدة
          </button>
        </div>
      )}
    </div>
  );
};