import 'package:supabase_flutter/supabase_flutter.dart' hide Provider;

export 'database/database.dart';

const _kSupabaseUrl = 'https://yjjwhjqvqivkyhdnnrfh.supabase.co';
const _kSupabaseAnonKey =
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqandoanF2cWl2a3loZG5ucmZoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTE4MzM3ODQsImV4cCI6MjAyNzQwOTc4NH0.vfbrBLYALeJqbrlFQFBVaEjxMob91DSh5Rpj912PvdA';

class SupaFlow {
  SupaFlow._();

  static SupaFlow? _instance;
  static SupaFlow get instance => _instance ??= SupaFlow._();

  final _supabase = Supabase.instance.client;
  static SupabaseClient get client => instance._supabase;

  static Future initialize() => Supabase.initialize(
        url: _kSupabaseUrl,
        anonKey: _kSupabaseAnonKey,
        debug: false,
      );
}
