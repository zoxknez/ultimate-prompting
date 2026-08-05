using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        // Vulnerable: signature validation, issuer validation, and audience
        // validation are all explicitly turned off. Any caller can craft a
        // JWT with an arbitrary payload - including any user id or role
        // claim - sign it with nothing (or anything), and this middleware
        // will accept it as a fully authenticated request. This is
        // equivalent to having no authentication at all.
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuerSigningKey = false,
            ValidateIssuer = false,
            ValidateAudience = false,
            ValidateLifetime = false,
        };
    });

var app = builder.Build();
app.UseAuthentication();
app.UseAuthorization();
app.Run();
