import React, { useState } from 'react';
import { Calendar, AlertCircle, CheckCircle, Filter, Users } from 'lucide-react';
import { useData } from '../context/DataContext';

export const AttendanceView: React.FC = () => {
  const { absences, students, loading } = useData();
  const [selectedGroup, setSelectedGroup] = useState('');
  const [selectedDate, setSelectedDate] = useState('');

  const filteredAbsences = absences.filter(absence => {
    const groupMatch = !selectedGroup || absence.المجموعة === selectedGroup;
    const dateMatch = !selectedDate || absence.التاريخ === selectedDate;
    return groupMatch && dateMatch;
  });

  const getUniqueGroups = () => {
    return [...new Set(students.map(student => student.المجموعة))];
  };

  const getUniqueDates = () => {
    return [...new Set(absences.map(absence => absence.التاريخ))].sort().reverse();
  };

  const getAttendanceStats = () => {
    const totalStudents = students.length;
    const absentToday = absences.filter(absence => 
      absence.التاريخ === new Date().toISOString().split('T')[0]
    ).length;
    const presentToday = totalStudents - absentToday;
    const attendanceRate = totalStudents > 0 ? (presentToday / totalStudents) * 100 : 0;

    return { totalStudents, absentToday, presentToday, attendanceRate };
  };

  const stats = getAttendanceStats();

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
          <h1 className="text-2xl font-bold text-gray-900">متابعة الحضور والغياب</h1>
          <p className="text-gray-600">تتبع حضور الطلاب وإدارة الغياب</p>
        </div>
        <button className="btn-primary flex items-center gap-2">
          <Calendar className="w-5 h-5" />
          تسجيل حضور جديد
        </button>
      </div>

      {/* Attendance Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="card bg-gradient-to-br from-primary-50 to-primary-100 border-primary-200">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-primary-700">إجمالي الطلاب</p>
              <p className="text-2xl font-bold text-primary-900">{stats.totalStudents}</p>
            </div>
            <Users className="w-8 h-8 text-primary-600" />
          </div>
        </div>

        <div className="card bg-gradient-to-br from-success-50 to-success-100 border-success-200">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-success-700">الحاضرون اليوم</p>
              <p className="text-2xl font-bold text-success-900">{stats.presentToday}</p>
            </div>
            <CheckCircle className="w-8 h-8 text-success-600" />
          </div>
        </div>

        <div className="card bg-gradient-to-br from-warning-50 to-warning-100 border-warning-200">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-warning-700">الغائبون اليوم</p>
              <p className="text-2xl font-bold text-warning-900">{stats.absentToday}</p>
            </div>
            <AlertCircle className="w-8 h-8 text-warning-600" />
          </div>
        </div>

        <div className="card bg-gradient-to-br from-gray-50 to-gray-100 border-gray-200">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-700">نسبة الحضور</p>
              <p className="text-2xl font-bold text-gray-900">{stats.attendanceRate.toFixed(1)}%</p>
            </div>
            <BarChart3 className="w-8 h-8 text-gray-600" />
          </div>
        </div>
      </div>

      {/* Filters */}
      <div className="card">
        <div className="flex items-center gap-4 mb-4">
          <Filter className="w-5 h-5 text-gray-600" />
          <h3 className="text-lg font-semibold text-gray-900">تصفية البيانات</h3>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <select
            value={selectedGroup}
            onChange={(e) => setSelectedGroup(e.target.value)}
            className="input-field"
          >
            <option value="">جميع المجموعات</option>
            {getUniqueGroups().map(group => (
              <option key={group} value={group}>{group}</option>
            ))}
          </select>
          
          <select
            value={selectedDate}
            onChange={(e) => setSelectedDate(e.target.value)}
            className="input-field"
          >
            <option value="">جميع التواريخ</option>
            {getUniqueDates().map(date => (
              <option key={date} value={date}>
                {new Date(date).toLocaleDateString('ar-EG')}
              </option>
            ))}
          </select>
          
          <button 
            onClick={() => {
              setSelectedGroup('');
              setSelectedDate('');
            }}
            className="btn-secondary"
          >
            إعادة تعيين
          </button>
        </div>
      </div>

      {/* Attendance Records */}
      <div className="card">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">سجل الغياب</h3>
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="table-header">
              <tr>
                <th className="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">
                  الطالب
                </th>
                <th className="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">
                  المجموعة
                </th>
                <th className="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">
                  الحصة
                </th>
                <th className="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">
                  التاريخ
                </th>
                <th className="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">
                  الحالة
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {filteredAbsences.map((absence, index) => (
                <tr key={index} className="hover:bg-gray-50 transition-colors duration-150">
                  <td className="table-cell">
                    <div className="flex items-center">
                      <div className="w-8 h-8 bg-error-100 rounded-full flex items-center justify-center ml-3">
                        <span className="text-error-700 font-semibold text-sm">
                          {absence.الاسم.charAt(0)}
                        </span>
                      </div>
                      <span className="font-medium">{absence.الاسم}</span>
                    </div>
                  </td>
                  <td className="table-cell">
                    <span className="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-800">
                      {absence.المجموعة}
                    </span>
                  </td>
                  <td className="table-cell">{absence.الحصة}</td>
                  <td className="table-cell">
                    {new Date(absence.التاريخ).toLocaleDateString('ar-EG')}
                  </td>
                  <td className="table-cell">
                    <span className="status-badge status-absent">
                      {absence.الحالة}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {filteredAbsences.length === 0 && (
          <div className="text-center py-12">
            <CheckCircle className="w-12 h-12 text-success-400 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-900 mb-2">لا توجد حالات غياب</h3>
            <p className="text-gray-500">جميع الطلاب حاضرون في الفترة المحددة</p>
          </div>
        )}
      </div>
    </div>
  );
};