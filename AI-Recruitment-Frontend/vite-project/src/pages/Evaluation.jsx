import { useEffect, useState } from "react";

export default function Evaluation() {

  const [report, setReport] = useState("");

useEffect(() => {

  const savedReport =
    localStorage.getItem(
      "evaluationReport"
    );
    console.log(savedReport);

  if (savedReport) {

    setReport(savedReport);

    const technical =
  savedReport.match(
    /Technical Score.*?\*\*(\d+)\*\*/is
  )?.[1] || "0";

const communication =
  savedReport.match(
    /Communication Score.*?\*\*(\d+)\*\*/is
  )?.[1] || "0";

const problem =
  savedReport.match(
    /Problem Solving Score.*?\*\*(\d+)\*\*/is
  )?.[1] || "0";

    localStorage.setItem(
      "technicalScore",
      technical
    );

    localStorage.setItem(
      "communicationScore",
      communication
    );

    localStorage.setItem(
      "problemScore",
      problem
    );

    let decision = "REJECT";

    const avg =
      (
        Number(technical) +
        Number(communication) +
        Number(problem)
      ) / 3;

    if (avg >= 75) {

      decision = "SELECT";

    } else if (avg >= 50) {

      decision = "CONSIDER";

    }

    localStorage.setItem(
      "recommendation",
      decision
    );

  }

}, []);

  return (

    <div className="p-8 text-white">

      <div className="mb-10">

        <h1 className="text-5xl font-bold">
          Candidate Evaluation
        </h1>

        <p className="text-slate-400 mt-3">
          AI generated evaluation based
          on interview performance.
        </p>

      </div>

      {/* Score Cards */}

      <div className="grid grid-cols-3 gap-6 mb-8">

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

          <h3 className="text-slate-400">
            Technical Score
          </h3>

          <p className="text-4xl font-bold text-cyan-400 mt-2">
            {
  report
    ? localStorage.getItem("technicalScore")
    : "--"
}
          </p>

        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

          <h3 className="text-slate-400">
            Communication Score
          </h3>

          <p className="text-4xl font-bold text-green-400 mt-2">
            {localStorage.getItem("communicationScore") || "--"}
          </p>

        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

          <h3 className="text-slate-400">
            Problem Solving Score
          </h3>

          <p className="text-4xl font-bold text-yellow-400 mt-2">
            {localStorage.getItem("problemScore") || "--"}
          </p>

        </div>

      </div>

      {/* Report */}

      <div
        className="
          bg-slate-900
          border
          border-slate-800
          rounded-3xl
          p-8
        "
      >

        <pre
          className="
            whitespace-pre-wrap
            text-slate-300
            leading-8
          "
        >
          {report}
        </pre>

      </div>

      <button
        onClick={() =>
          window.location.href =
            "/reports"
        }
        className="
          mt-8
          bg-cyan-500
          hover:bg-cyan-600
          px-8
          py-4
          rounded-xl
          font-semibold
        "
      >
        Continue To Reports
      </button>

    </div>

  );
}