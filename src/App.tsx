import React, { useState, useEffect } from 'react';
import { Header } from './components/Header';
import { Sidebar } from './components/Sidebar';
import { Dashboard } from './components/Dashboard';
import { StudentsView } from './components/StudentsView';
import { ExamsView } from './components/ExamsView';
import { AttendanceView } from './components/AttendanceView';
import { GroupsView } from './components/GroupsView';
import { DataProvider } from './context/DataContext';

export type ViewType = 'dashboard' | 'students' | 'exams' | 'attendance' | 'groups';

function App() {
  const [currentView, setCurrentView] = useState<ViewType>('dashboard');
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const renderCurrentView = () => {
    switch (currentView) {
      case 'dashboard':
        return <Dashboard />;
      case 'students':
        return <StudentsView />;
      case 'exams':
        return <ExamsView />;
      case 'attendance':
        return <AttendanceView />;
      case 'groups':
        return <GroupsView />;
      default:
        return <Dashboard />;
    }
  };

  return (
    <DataProvider>
      <div className="min-h-screen bg-gray-50 flex">
        <Sidebar 
          currentView={currentView} 
          onViewChange={setCurrentView}
          isOpen={sidebarOpen}
          onToggle={() => setSidebarOpen(!sidebarOpen)}
        />
        
        <div className="flex-1 flex flex-col overflow-hidden">
          <Header 
            onMenuClick={() => setSidebarOpen(!sidebarOpen)}
            currentView={currentView}
          />
          
          <main className="flex-1 overflow-auto p-6">
            <div className="max-w-7xl mx-auto">
              {renderCurrentView()}
            </div>
          </main>
        </div>
      </div>
    </DataProvider>
  );
}

export default App;