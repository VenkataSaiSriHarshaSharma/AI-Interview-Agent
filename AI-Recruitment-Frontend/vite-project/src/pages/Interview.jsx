import { useState } from "react";
import api from "../services/api";

export default function Interview() {
  const [role, setRole] = useState("");

  const [questions, setQuestions] = useState([]);

  const [answers, setAnswers] = useState([]);

  const [loading, setLoading] = useState(false);

  const [evaluating, setEvaluating] = useState(false);

  const generateQuestions = async () => {
    if (!role.trim()) {
      alert("Please enter a role");
      return;
    }

    try {
      setLoading(true);
      
      console.log("Role:", role);

      const response = await api.post(
        "/generate-questions",
        {
          role: role,
          question_count: 5,
        }
      );

      console.log(response.data);

      setQuestions(response.data.questions);

      setAnswers(
        new Array(
          response.data.questions.length
        ).fill("")
      );
    } catch (error) {
      console.error(error);
      alert("Failed to generate questions");
    } finally {
      setLoading(false);
    }
  };

  const updateAnswer = (index, value) => {
    const updatedAnswers = [...answers];

    updatedAnswers[index] = value;

    setAnswers(updatedAnswers);
  };

  const generateEvaluation = async () => {
    try {
      setEvaluating(true);

      const candidateProfile = {
        name: "Candidate",
        role: role,
        experience: "Fresher",
      };

      const formattedAnswers = questions.map(
        (question, index) => ({
          question: question,
          answer: answers[index],
        })
      );

      const response = await api.post(
        "/evaluate",
        {
          candidate_profile: candidateProfile,
          answers: formattedAnswers,
        }
      );

      localStorage.setItem(
        "evaluationReport",
        response.data.report
      );

      window.location.href = "/evaluation";
    } catch (error) {
      console.error(error);
      alert("Evaluation failed");
    } finally {
      setEvaluating(false);
    }
  };

  return (
    <div className="p-8 text-white">
      {/* HEADER */}

      <div className="mb-10">
        <h1 className="text-5xl font-bold">
          AI Interview Workspace
        </h1>

        <p className="text-slate-400 mt-3">
          Generate role-based interview
          questions and evaluate candidates
          using AI.
        </p>
      </div>

      {/* ROLE INPUT */}

      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-8">

        <h2 className="text-2xl font-semibold mb-5">
          Interview Setup
        </h2>

        <select
  value={role}
  onChange={(e) =>
    setRole(e.target.value)
  }
  className="
    w-full
    bg-slate-950
    border
    border-slate-700
    rounded-xl
    px-4
    py-4
    text-white
  "
>
  <option value="">
    Select Role
  </option>

  <option value="Python Developer">
    Python Developer
  </option>

  <option value="Java Developer">
    Java Developer
  </option>

  <option value="AI Engineer">
    AI Engineer
  </option>

  <option value="Data Analyst">
    Data Analyst
  </option>

  <option value="Full Stack Developer">
    Full Stack Developer
  </option>

  <option value="Cyber Security Analyst">
    Cyber Security Analyst
  </option>

  <option value="Cloud Engineer">
    Cloud Engineer
  </option>

  <option value="DevOps Engineer">
    DevOps Engineer
  </option>

  <option value="Backend Developer">
    Backend Developer
  </option>

  <option value="Frontend Developer">
    Frontend Developer
  </option>

  <option value="Software Engineer">
    Software Engineer
  </option>

  <option value="Data Engineer">
    Data Engineer
  </option>

  <option value="Business Analyst">
    Business Analyst
  </option>

  <option value="QA Engineer">
    QA Engineer
  </option>

  <option value="Mobile App Developer">
    Mobile App Developer
  </option>
</select>

        <button
          onClick={generateQuestions}
          disabled={loading}
          className="
            mt-6
            bg-cyan-500
            hover:bg-cyan-600
            px-8
            py-4
            rounded-xl
            font-semibold
            transition
          "
        >
          {loading
            ? "Generating Questions..."
            : "Generate Questions"}
        </button>
      </div>

      {/* QUESTIONS */}

      {questions.length > 0 && (
        <div className="mt-10">

          <h2 className="text-3xl font-bold mb-6">
            Interview Questions
          </h2>

          {questions.map(
            (question, index) => (
              <div
                key={index}
                className="
                  bg-slate-900
                  border
                  border-slate-800
                  rounded-3xl
                  p-6
                  mb-6
                "
              >
                <h3 className="text-xl font-bold mb-4">
                  Question {index + 1}
                </h3>

                <p className="text-slate-300 mb-5">
                  {question}
                </p>

                <textarea
                  rows="5"
                  value={answers[index]}
                  onChange={(e) =>
                    updateAnswer(
                      index,
                      e.target.value
                    )
                  }
                  placeholder="Enter candidate answer..."
                  className="
                    w-full
                    bg-slate-950
                    border
                    border-slate-700
                    rounded-xl
                    p-4
                    text-white
                    outline-none
                    focus:border-cyan-400
                  "
                />
              </div>
            )
          )}

          <button
            onClick={generateEvaluation}
            disabled={evaluating}
            className="
              bg-green-500
              hover:bg-green-600
              px-8
              py-4
              rounded-xl
              font-semibold
              transition
            "
          >
            {evaluating
              ? "Generating Evaluation..."
              : "Generate Evaluation"}
          </button>
        </div>
      )}
    </div>
  );
}