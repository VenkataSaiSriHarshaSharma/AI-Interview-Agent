import Sidebar from "../components/Sidebar";

export default function MainLayout({
  children
}) {

  return (

    <div className="flex min-h-screen bg-slate-950">

      <Sidebar />

      <main className="flex-1">
        {children}
      </main>

    </div>

  );
}