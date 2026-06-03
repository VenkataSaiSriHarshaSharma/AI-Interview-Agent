import CandidateCard from "./CandidateCard";

export default function RecentCandidates() {
  return (

    <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">

      <h2 className="text-xl font-bold text-white mb-6">
        Recent Candidates
      </h2>

      <div className="grid grid-cols-3 gap-4">

        <CandidateCard
          name="John Smith"
          role="Python Developer"
          score="91"
          status="Selected"
        />

        <CandidateCard
          name="Sarah Lee"
          role="AI Engineer"
          score="87"
          status="Consider"
        />

        <CandidateCard
          name="Michael"
          role="Java Developer"
          score="93"
          status="Selected"
        />

      </div>

    </div>
  );
}