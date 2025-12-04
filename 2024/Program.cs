using TUnit.Core;
using TUnit.Engine.Extensions;
using Microsoft.Testing.Platform.Builder;

internal class Program
{
    #pragma warning disable TUnit0034
    private static async Task<int> Main(string[] args)
    {
        if (args.Length > 0 && (args[0] == "--test" || args[0] == "-t"))
        {
            // --- Run Unit Tests ---
            var testArgs = args.Skip(1).ToArray();
            
            var builder = await TestApplication.CreateBuilderAsync(testArgs);
            builder.AddTUnit();
            
            using var app = await builder.BuildAsync();
            return await app.RunAsync();
        }

        // --- Standard Application Logic ---
        Console.WriteLine("--- Running Console App ---");
        
        // Add your solution code here
        // Example: var day01 = new AdventOfCode.Solutions.Day01();
        
        return 0;
    }
}
