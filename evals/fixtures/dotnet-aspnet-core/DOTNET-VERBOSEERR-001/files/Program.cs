var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Vulnerable: the developer exception page is registered unconditionally,
// not gated behind app.Environment.IsDevelopment(). In production this
// renders full stack traces, local file paths, and request details to any
// client that triggers an unhandled exception.
app.UseDeveloperExceptionPage();

app.MapGet("/", () => "OK");

app.Run();
