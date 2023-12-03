import "./App.css";
import Background from "./components/Background";
// import Background from "./components/Background";

function handleSubmit(e) {
  e.preventDefault();
}

function App() {
  return (
    <>
      <div
        id="home-page"
        className="h-[100vh] w-[100vw] flex justify-center items-center"
      >
        <Background />
        <form
          className="flex flex-col items-center justify-center gap-10"
          onSubmit={handleSubmit}
        >
          <p className="text-[#eb5967] text-6xl ">
            Tell us how you are feeling
          </p>
          <input
            className="h-[40px] w-[500px] bg-[#0e202f] text-center text-[#FA7268] placeholder:text-[#eb5967]"
            placeholder="..."
          ></input>
          <button className="border-[1px] border-[#eb5967] rounded-full text-[#eb5967] px-4 py-2 hover:text-white hover:bg-[#eb5967] transition-all">
            Continue
          </button>
        </form>
      </div>
    </>
  );
}

export default App;
