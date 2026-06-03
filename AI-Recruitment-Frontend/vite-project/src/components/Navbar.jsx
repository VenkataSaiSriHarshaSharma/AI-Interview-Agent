export default function Navbar() {
  return (
    <div className="flex justify-between items-center mb-8">

      <div>
        <h1 className="text-4xl font-bold text-white">
          Dashboard
        </h1>

        <p className="text-slate-400 mt-2">
          Welcome back recruiter
        </p>
      </div>

      <div className="h-12 w-12 rounded-full bg-cyan-500 flex items-center justify-center text-white font-bold">
        A
      </div>

    </div>
  );
}