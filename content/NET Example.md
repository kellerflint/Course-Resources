Model
```cs
public class Book
{
    public int Id { get; set; }
    public string Title { get; set; }
    public string Author { get; set; }
    public int Year { get; set; }
}
```

Service
```cs
public interface IBookRepository
{
    Book GetById(int id);
    void Add(Book book);
    void Update(Book book);
    void SaveChanges();
}
```

```cs
public interface IBookService
{
    Task<Book> GetBookByIdAsync(int id);
    Task<Book> AddBookAsync(Book book);
    Task<Book> UpdateBookAsync(int id, Book book);
}
```

```cs
public class BookService : IBookService
{
    private readonly IBookRepository _bookRepository;

    public BookService(IBookRepository bookRepository)
    {
        _bookRepository = bookRepository;
    }

    public Book GetBookById(int id)
    {
        return _bookRepository.GetById(id);
    }

    public Book AddBook(Book book)
    {
        _bookRepository.Add(book);
        _bookRepository.SaveChanges();
        return book;
    }

    public Book UpdateBook(int id, Book updatedBook)
    {
        var book = _bookRepository.GetById(id);
        if (book != null)
        {
            book.Title = updatedBook.Title;
            book.Author = updatedBook.Author;
            book.Year = updatedBook.Year;
            _bookRepository.Update(book);
            _bookRepository.SaveChanges();
        }
        return book;
    }
}
```


Controller
```cs
using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("[controller]")]
public class BooksController : ControllerBase
{
    private readonly IBookService _bookService;

    public BooksController(IBookService bookService)
    {
        _bookService = bookService;
    }

    [HttpGet("{id}")]
    public IActionResult Get(int id)
    {
        var book = _bookService.GetBookById(id);
        if (book == null) return NotFound();
        return Ok(book);
    }

    [HttpPost]
    public IActionResult Post([FromBody] Book book)
    {
        var newBook = _bookService.AddBook(book);
        return CreatedAtAction(nameof(Get), new { id = newBook.Id }, newBook);
    }

    [HttpPut("{id}")]
    public IActionResult Put(int id, [FromBody] Book book)
    {
        var updatedBook = _bookService.UpdateBook(id, book);
        if (updatedBook == null) return NotFound();
        return Ok(updatedBook);
    }
}
```

Program.cs (application entry point)
```cs
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddScoped<IBookService, BookService>();
builder.Services.AddScoped<IBookRepository, BookRepository>();


var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseDeveloperExceptionPage();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();

```