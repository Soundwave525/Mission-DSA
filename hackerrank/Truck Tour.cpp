int truckTour(vector < vector < int >> petrolpumps){
  long long total_fuel = 0;
  long long curr_fuel = 0;
  int start = 0;

  for(int i = 0; i < petrolpumps.size(); i++){
    int petrol = petrolpumps[i][0];
    int distance = petrolpumps[i][1];

    total_fuel += petrol - distance;
    curr_fuel += petrol - distance;

    if (curr_fuel < 0){
      start = i + 1;
      curr_fuel = 0;
    }
  }
  return start;
}
