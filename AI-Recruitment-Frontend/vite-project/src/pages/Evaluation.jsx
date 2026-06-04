import { useEffect, useState } from "react";

export default function Evaluation() {

  const [report, setReport] = useState("");

  useEffect(() => {

    const savedReport =
      localStorage.getItem(
        "evaluationReport"
      );

    if (savedReport) {
      setReport(savedReport);
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