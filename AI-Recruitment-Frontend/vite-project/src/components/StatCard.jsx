export default function StatCard({
  title,
  value
}) {

  return (

    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">

      <p className="text-slate-400">
        {title}
      </p>

      <h2 className="text-4xl font-bold text-cyan-400 mt-4">
        {value}
      </h2>

    </div>

  );
}