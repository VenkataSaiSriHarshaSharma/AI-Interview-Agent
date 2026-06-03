import { useState } from "react";
import api from "../services/api";

export default function Interview() {

  const [role, setRole] = useState("");
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState([]);

  const generateQuestions = async () => {

    const response = await api.post(
      "/generate-questions",
      {
        role,
        question_count: 5,
      }
    );

    setQuestions(
      response.data.questions
    );

    setAnswers(
      new Array(
        response.data.questions.length
      ).fill("")
    );
  };

  const updateAnswer = (
    index,
    value
  ) => {

    const updated = [...answers];

    updated[index] = value;

    setAnswers(updated);
  };

  return (

    <div className="p-8 text-white">

      <h1 className="text-5xl font-bold mb-6">
        AI Interview Workspace
      </h1>

      <input
        placeholder="Target Role"
        className="
          bg-slate-900
          border
          border-slate-700
          px-4
          py-3
          rounded-xl
          mb-4
          w-full
        "
        onChange={(e)=>
          setRole(
            e.target.value
          )
        }
      />

      <button
        onClick={generateQuestions}
        className="
          bg-cyan-500
          px-6
          py-3
          rounded-xl
        "
      >
        Generate Questions
      </button>

      <div className="mt-8">

        {questions.map(
          (
            question,
            index
          ) => (

            <div
              key={index}
              className="
                bg-slate-900
                p-6
                rounded-2xl
                mb-6
              "
            >

              <h3 className="font-bold mb-4">
                Question {index + 1}
              </h3>

              <p>{question}</p>

              <textarea
                className="
                  mt-4
                  w-full
                  bg-slate-950
                  border
                  border-slate-700
                  rounded-xl
                  p-4
                "
                rows="4"
                value={answers[index]}
                onChange={(e)=>
                  updateAnswer(
                    index,
                    e.target.value
                  )
                }
              />

            </div>

          )
        )}

      </div>

    </div>

  );
}