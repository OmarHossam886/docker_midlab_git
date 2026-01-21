# Build stage
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build

WORKDIR /docker_midlab
COPY . .

RUN dotnet publish /worker/Worker.csproj -c Release -o /app

# Runtime stage
FROM mcr.microsoft.com/dotnet/runtime:7.0
WORKDIR /docker_midlab
COPY --from=build /docker_midlab .

ENTRYPOINT ["dotnet", "Worker.dll"]
