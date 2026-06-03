export default function CandidateCard({
  name,
  role,
  score,
  status
}) {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 hover:border-cyan-500 transition">

      <h3 className="text-white text-lg font-semibold">
        {name}
      </h3>

      <p className="text-slate-400 mt-2">
        {role}
      </p>

      <div className="flex justify-between mt-5">

        <span className="text-cyan-400 font-bold">
          Score: {score}
        </span>

        <span className="text-green-400">
          {status}
        </span>

      </div>

    </div>
  );
}