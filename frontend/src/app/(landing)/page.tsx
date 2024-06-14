export default function Home() {

  

  return (
    <div>
      <h1>Main Page</h1>
      <form action="/api/v2/test" method="post" accept-charset="utf-8" encType="multipart/form-data">
				<label htmlFor="mp3">Image</label>
				<input type="file" name="image" accept="image/*" />
				<input type="submit" value="submit"/>
			</form>
    </div>
  );
}
