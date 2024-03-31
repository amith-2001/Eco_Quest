import '../database.dart';

class SustainAppTable extends SupabaseTable<SustainAppRow> {
  @override
  String get tableName => 'sustainApp';

  @override
  SustainAppRow createRow(Map<String, dynamic> data) => SustainAppRow(data);
}

class SustainAppRow extends SupabaseDataRow {
  SustainAppRow(super.data);

  @override
  SupabaseTable get table => SustainAppTable();

  int get id => getField<int>('id')!;
  set id(int value) => setField<int>('id', value);

  DateTime get createdAt => getField<DateTime>('created_at')!;
  set createdAt(DateTime value) => setField<DateTime>('created_at', value);

  String? get mcq => getField<String>('mcq');
  set mcq(String? value) => setField<String>('mcq', value);

  String? get energy => getField<String>('energy');
  set energy(String? value) => setField<String>('energy', value);
}
