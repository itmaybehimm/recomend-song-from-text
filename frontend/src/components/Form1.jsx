function Form1(props) {
  return (
    <form
      className="flex flex-col items-center justify-center gap-10"
      onSubmit={props.handleSubmit}
    >
      <p className="text-[#eb5967] text-6xl ">Enter spotify username</p>
      <input
        className="h-[40px] w-[500px] bg-[#0e202f] text-center text-[#FA7268] placeholder:text-[#eb5967]"
        name="string"
        placeholder="..."
        value={props.username}
        onChange={(e) => props.setUsername(e.target.value)}
      ></input>
      <button
        className="border-[1px] border-[#eb5967] rounded-full text-[#eb5967] px-4 py-2 hover:text-white hover:bg-[#eb5967] transition-all"
        onClick={() => props.setFormState(1)}
      >
        Continue
      </button>
    </form>
  );
}

export default Form1;
